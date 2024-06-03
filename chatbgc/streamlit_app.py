import argparse
import logging
import os
import time

import streamlit as st
from code_editor import code_editor

from chatbgc.vanna_calls import (
    generate_followup_cached,
    generate_plot_cached,
    generate_plotly_code_cached,
    generate_questions_cached,
    generate_sql_cached,
    generate_summary_cached,
    is_sql_valid_cached,
    run_sql_cached,
    setup_vanna,
    should_generate_chart_cached,
)


def start_streamlit_app():
    """
    This function starts the Streamlit application for ChatBGC.

    It sets up the Streamlit page layout, creates a sidebar with output settings,
    and initializes the chat interface. It also handles the interaction with the
    user, including receiving the user's question, generating and displaying the
    SQL query, running the query, and displaying the results.

    Environment variables are used to configure the application. The following
    environment variables are used:
    - CHATBGC_DUCKDB_PATH: The path to the DuckDB database.
    - CHATBGC_MODEL: The model to use for generating SQL queries. Defaults to 'llama3'.
    - CHATBGC_LLM_TYPE: The type of the LLM. Defaults to 'ollama'.

    No arguments are required to call this function.

    This function does not return a value.
    """
    # Get the parameters from the environment variables
    duckdb_path = os.getenv("CHATBGC_DUCKDB_PATH")
    model = os.getenv("CHATBGC_MODEL", "llama3")
    llm_type = os.getenv("CHATBGC_LLM_TYPE", "ollama")

    # Log the values of the environment variables
    logging.info(f"CHATBGC_DUCKDB_PATH: {duckdb_path}")
    logging.info(f"CHATBGC_MODEL: {model}")
    logging.info(f"CHATBGC_LLM_TYPE: {llm_type}")

    # Streamlit start
    avatar_url = "https://raw.githubusercontent.com/NBChub/chatBGC/main/chatbgc/assets/bgcflow_logo.png"

    st.set_page_config(layout="wide")

    st.sidebar.title("Output Settings")
    st.sidebar.checkbox("Show SQL", value=True, key="show_sql")
    st.sidebar.checkbox("Show Table", value=True, key="show_table")
    st.sidebar.checkbox("Show Plotly Code", value=True, key="show_plotly_code")
    st.sidebar.checkbox("Show Chart", value=True, key="show_chart")
    st.sidebar.checkbox("Show Summary", value=True, key="show_summary")
    st.sidebar.checkbox("Show Follow-up Questions", value=True, key="show_followup")
    st.sidebar.button(
        "Reset", on_click=lambda: set_question(None), use_container_width=True
    )

    st.title("ChatBGC")
    # st.sidebar.write(st.session_state)

    def set_question(question):
        st.session_state["my_question"] = question

    # start vanna
    vn = setup_vanna(duckdb_path=duckdb_path, model=model, llm_type=llm_type)

    assistant_message_suggested = st.chat_message("assistant", avatar=avatar_url)
    if assistant_message_suggested.button("Click to show suggested questions"):
        st.session_state["my_question"] = None
        questions = generate_questions_cached(vn)
        for i, question in enumerate(questions):
            time.sleep(0.05)
            st.button(
                question,
                on_click=set_question,
                args=(question,),
            )

    my_question = st.session_state.get("my_question", default=None)

    if my_question is None:
        my_question = st.chat_input(
            "Ask me a question about your data",
        )

    if my_question:
        st.session_state["my_question"] = my_question
        user_message = st.chat_message("user")
        user_message.write(f"{my_question}")

        sql = generate_sql_cached(vn, question=my_question)

        if sql:
            if is_sql_valid_cached(vn, sql=sql):
                if st.session_state.get("show_sql", True):
                    assistant_message_sql = st.chat_message(
                        "assistant", avatar=avatar_url
                    )
                    assistant_message_sql.code(sql, language="sql", line_numbers=True)
            else:
                assistant_message = st.chat_message("assistant", avatar=avatar_url)
                assistant_message.write(sql)
                st.stop()

            df = run_sql_cached(vn, sql=sql)

            if df is not None:
                st.session_state["df"] = df

            if st.session_state.get("df") is not None:
                if st.session_state.get("show_table", True):
                    df = st.session_state.get("df")
                    assistant_message_table = st.chat_message(
                        "assistant",
                        avatar=avatar_url,
                    )
                    if len(df) > 10:
                        assistant_message_table.text("First 10 rows of data")
                        assistant_message_table.dataframe(df.head(10))
                    else:
                        assistant_message_table.dataframe(df)

                if should_generate_chart_cached(
                    vn, question=my_question, sql=sql, df=df
                ):

                    code = generate_plotly_code_cached(
                        vn, question=my_question, sql=sql, df=df
                    )

                    if st.session_state.get("show_plotly_code", False):
                        assistant_message_plotly_code = st.chat_message(
                            "assistant",
                            avatar=avatar_url,
                        )
                        assistant_message_plotly_code.code(
                            code, language="python", line_numbers=True
                        )

                    if code is not None and code != "":
                        if st.session_state.get("show_chart", True):
                            assistant_message_chart = st.chat_message(
                                "assistant",
                                avatar=avatar_url,
                            )
                            fig = generate_plot_cached(vn, code=code, df=df)
                            if fig is not None:
                                assistant_message_chart.plotly_chart(fig)
                            else:
                                assistant_message_chart.error(
                                    "I couldn't generate a chart"
                                )

                if st.session_state.get("show_summary", True):
                    assistant_message_summary = st.chat_message(
                        "assistant",
                        avatar=avatar_url,
                    )
                    summary = generate_summary_cached(vn, question=my_question, df=df)
                    if summary is not None:
                        assistant_message_summary.text(summary)

                if st.session_state.get("show_followup", True):
                    assistant_message_followup = st.chat_message(
                        "assistant",
                        avatar=avatar_url,
                    )
                    followup_questions = generate_followup_cached(
                        vn, question=my_question, sql=sql, df=df
                    )
                    st.session_state["df"] = None

                    if len(followup_questions) > 0:
                        assistant_message_followup.text(
                            "Here are some possible follow-up questions"
                        )
                        # Print the first 5 follow-up questions
                        for question in followup_questions[:5]:
                            assistant_message_followup.button(
                                question, on_click=set_question, args=(question,)
                            )

        else:
            assistant_message_error = st.chat_message("assistant", avatar=avatar_url)
            assistant_message_error.error(
                "I wasn't able to generate SQL for that question"
            )


start_streamlit_app()
