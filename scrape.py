import requests
from bs4 import BeautifulSoup

def scrape_response_sheet(url):
    """
    Scrapes the JEE Mains response sheet, extracts questions, subjects, and student responses.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Save the scraped HTML for debugging
    with open("scraped_page.html", "w", encoding="utf-8") as file:
        file.write(str(soup))

    # Extract Exam Date & Slot
    exam_date = soup.find("td", string="Test Date").find_next_sibling("td").text.strip()
    exam_time = soup.find("td", string="Test Time").find_next_sibling("td").text.strip()
    exam_slot = exam_time.split("-")[0].strip()

    questions = []
    current_subject = None  # Track subject based on section headers

    # Iterate through all elements in the response sheet
    for element in soup.find_all(["span", "div"], class_=["bold", "question-pnl"]):
        # Detect section headers (Physics, Chemistry, Mathematics) and merge Section A & B
        if element.name == "span" and "Section" in element.text:
            if "Physics" in element.text:
                current_subject = "Physics"
            elif "Chemistry" in element.text:
                current_subject = "Chemistry"
            elif "Mathematics" in element.text:
                current_subject = "Mathematics"

        # Detect question panels
        elif element.name == "div" and "question-pnl" in element.get("class", []):
            q_id = element.find("td", string="Question ID :").find_next_sibling("td").text.strip()
            q_type = element.find("td", string="Question Type :").find_next_sibling("td").text.strip()
            status = element.find("td", string="Status :").find_next_sibling("td").text.strip()

            if q_type == "MCQ":
                chosen_option = element.find("td", string="Chosen Option :").find_next_sibling("td").text.strip()
                option_ids = [element.find("td", string=f"Option {i} ID :").find_next_sibling("td").text.strip() for i in range(1, 5)]

                questions.append({
                    "question_id": q_id,
                    "question_type": q_type,
                    "subject": current_subject,  # Assign question to detected subject
                    "option_ids": option_ids,
                    "chosen_option": chosen_option if status == "Answered" else "--",
                    "status": status
                })
            elif q_type == "SA":
                given_answer = element.find("td", string="Given Answer :").find_next_sibling("td").text.strip()
                questions.append({
                    "question_id": q_id,
                    "question_type": q_type,
                    "subject": current_subject,  # Assign question to detected subject
                    "given_answer": given_answer if status == "Answered" else "--",
                    "status": status
                })

    return {"exam_date": exam_date, "slot_time": exam_slot, "questions": questions}
