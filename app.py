import streamlit as st
import mysql.connector
import pandas as pd
from mysql.connector import IntegrityError, Error

# MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="noorfatima#01",
        database="project"
    )

st.title("📊 OBE Rubrics Management System")

menu = ["Home", "Manage Students", "Manage CLOs", "Manage Rubrics", "Manage Assessments",
        "Manage Rubric Levels", "Reports"]
choice = st.sidebar.selectbox("Menu", menu)

# --- Manage Students ---
if choice == "Manage Students":
    st.header("👨‍🎓 Manage Students")

    with st.form("add_student"):
        student_id = st.number_input("Student ID", min_value=1, step=1)
        name = st.text_input("Name")
        reg_no = st.text_input("Registration Number")
        section = st.text_input("Section")
        submit = st.form_submit_button("Add Student")

    if submit:
        if not name.strip():
            st.warning("Please enter a valid name.")
        elif not reg_no.strip():
            st.warning("Please enter a registration number.")
        elif not section.strip():
            st.warning("Please enter a section.")
        else:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO Student (student_id, name, reg_no, section) VALUES (%s, %s, %s, %s)",
                    (student_id, name.strip(), reg_no.strip(), section.strip())
                )
                conn.commit()
                st.success("✅ Student added successfully!")
            except IntegrityError:
                st.error("❌ Student ID already exists. Please enter a unique Student ID.")
            except Error as e:
                st.error(f"❌ Database error: {e}")
            finally:
                cursor.close()
                conn.close()

    if st.checkbox("📋 Show all students"):
        try:
            conn = get_connection()
            df = pd.read_sql("SELECT * FROM Student", conn)
            st.dataframe(df)
        except Error as e:
            st.error(f"❌ Failed to load students: {e}")
        finally:
            conn.close()

# --- Manage CLOs ---
elif choice == "Manage CLOs":
    st.header("📌 Manage CLOs")

    with st.form("add_clo"):
        clo_id = st.number_input("CLO ID", min_value=1, step=1)
        desc = st.text_area("CLO Description")
        submit = st.form_submit_button("Add CLO")

    if submit:
        if not desc.strip():
            st.warning("Please enter a CLO description.")
        else:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO CLO (clo_id, description) VALUES (%s, %s)", (clo_id, desc.strip()))
                conn.commit()
                st.success("✅ CLO added successfully!")
            except IntegrityError:
                st.error("❌ CLO ID already exists. Please enter a unique CLO ID.")
            except Error as e:
                st.error(f"❌ Database error: {e}")
            finally:
                cursor.close()
                conn.close()

    if st.checkbox("📋 Show all CLOs"):
        try:
            conn = get_connection()
            df = pd.read_sql("SELECT * FROM CLO", conn)
            st.dataframe(df)
        except Error as e:
            st.error(f"❌ Failed to load CLOs: {e}")
        finally:
            conn.close()

# --- Manage Rubrics ---
elif choice == "Manage Rubrics":
    st.header("📑 Manage Rubrics")

    try:
        conn = get_connection()
        clos = pd.read_sql("SELECT * FROM CLO", conn)
    except Error as e:
        st.error(f"❌ Failed to load CLOs: {e}")
        clos = pd.DataFrame()
    finally:
        conn.close()

    with st.form("add_rubric"):
        rubric_id = st.number_input("Rubric ID", min_value=1, step=1)
        description = st.text_area("Rubric Description")
        clo_id = st.selectbox("Select CLO", clos["clo_id"] if not clos.empty else [])
        submit = st.form_submit_button("Add Rubric")

    if submit:
        if not description.strip():
            st.warning("Please enter a rubric description.")
        elif clos.empty:
            st.warning("No CLOs available. Please add a CLO first.")
        else:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO Rubric (rubric_id, description, clo_id) VALUES (%s, %s, %s)",
                    (rubric_id, description.strip(), clo_id)
                )
                conn.commit()
                st.success("✅ Rubric added successfully!")
            except IntegrityError:
                st.error("❌ Rubric ID already exists. Please enter a unique Rubric ID.")
            except Error as e:
                st.error(f"❌ Database error: {e}")
            finally:
                cursor.close()
                conn.close()

    if st.checkbox("📋 Show all Rubrics"):
        try:
            conn = get_connection()
            df = pd.read_sql("SELECT * FROM Rubric", conn)
            st.dataframe(df)
        except Error as e:
            st.error(f"❌ Failed to load Rubrics: {e}")
        finally:
            conn.close()

# --- Manage Assessments ---
elif choice == "Manage Assessments":
    st.header("📝 Manage Assessments")

    with st.form("add_assessment"):
        assess_id = st.number_input("Assessment ID", min_value=1, step=1)
        title = st.text_input("Assessment Title")
        total_marks = st.number_input("Total Marks", min_value=1)
        submit = st.form_submit_button("Add Assessment")

    if submit:
        if not title.strip():
            st.warning("Please enter an assessment title.")
        else:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO Assessment (assess_id, title, total_marks) VALUES (%s, %s, %s)",
                    (assess_id, title.strip(), total_marks)
                )
                conn.commit()
                st.success("✅ Assessment added!")
            except IntegrityError:
                st.error("❌ Assessment ID already exists. Please enter a unique Assessment ID.")
            except Error as e:
                st.error(f"❌ Database error: {e}")
            finally:
                cursor.close()
                conn.close()

    if st.checkbox("📋 Show all Assessments"):
        try:
            conn = get_connection()
            df = pd.read_sql("SELECT * FROM Assessment", conn)
            st.dataframe(df)
        except Error as e:
            st.error(f"❌ Failed to load Assessments: {e}")
        finally:
            conn.close()

# --- Manage Rubric Levels ---
elif choice == "Manage Rubric Levels":
    st.header("📈 Manage Rubric Levels")

    try:
        conn = get_connection()
        rubrics = pd.read_sql("SELECT * FROM Rubric", conn)
    except Error as e:
        st.error(f"❌ Failed to load Rubrics: {e}")
        rubrics = pd.DataFrame()
    finally:
        conn.close()

    with st.form("add_level"):
        level_id = st.number_input("Level ID", min_value=1, step=1)
        level = st.selectbox("Level", [1, 2, 3, 4, 5])
        description = st.text_input("Level Description")
        rubric_id = st.selectbox("Select Rubric", rubrics["rubric_id"] if not rubrics.empty else [])
        submit = st.form_submit_button("Add Level")

    if submit:
        if not description.strip():
            st.warning("Please enter a level description.")
        elif rubrics.empty:
            st.warning("No Rubrics available. Please add a Rubric first.")
        else:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO RubricLevel (level_id, rubric_id, level, description) VALUES (%s, %s, %s, %s)",
                    (level_id, rubric_id, level, description.strip())
                )
                conn.commit()
                st.success("✅ Rubric Level added!")
            except IntegrityError:
                st.error("❌ Level ID already exists. Please enter a unique Level ID.")
            except Error as e:
                st.error(f"❌ Database error: {e}")
            finally:
                cursor.close()
                conn.close()

    if st.checkbox("📋 Show all Rubric Levels"):
        try:
            conn = get_connection()
            df = pd.read_sql("SELECT * FROM RubricLevel", conn)
            st.dataframe(df)
        except Error as e:
            st.error(f"❌ Failed to load Rubric Levels: {e}")
        finally:
            conn.close()

# --- Reports ---
elif choice == "Reports":
    st.header("📊 Reports")

    report_type = st.radio("Select Report Type", ["Evaluation Summary", "CLO-wise Class Result", "Assessment-wise Class Result"])

    conn = get_connection()

    if report_type == "Evaluation Summary":
        query = """
        SELECT s.name AS student, a.title AS assessment, rl.level
        FROM Evaluation e
        JOIN Student s ON e.student_id = s.student_id
        JOIN Assessment a ON e.assess_id = a.assess_id
        JOIN RubricLevel rl ON e.level_id = rl.level_id
        """
        df = pd.read_sql(query, conn)
        st.subheader("📋 Evaluation Summary")
        st.dataframe(df)

    elif report_type == "CLO-wise Class Result":
        query = """
        SELECT c.clo_id AS CLO_ID, s.name AS Student, e.eval_id AS Evaluation_ID, rl.level AS Rubric_Level
        FROM Evaluation e
        JOIN Student s ON s.student_id = e.student_id
        JOIN Rubric r ON r.rubric_id = e.rubric_id
        JOIN CLO c ON c.clo_id = r.clo_id
        JOIN RubricLevel rl ON rl.level_id = e.level_id
        """
        df = pd.read_sql(query, conn)
        st.subheader("📘 CLO-wise Class Result")
        st.dataframe(df)

    elif report_type == "Assessment-wise Class Result":
        query = """
        SELECT a.title AS Assessment, s.name AS Student, rl.level AS Rubric_Level
        FROM Evaluation e
        JOIN Assessment a ON a.assess_id = e.assess_id
        JOIN Student s ON s.student_id = e.student_id
        JOIN RubricLevel rl ON rl.level_id = e.level_id
        """
        df = pd.read_sql(query, conn)
        st.subheader("📝 Assessment-wise Class Result")
        st.dataframe(df)

    conn.close()
