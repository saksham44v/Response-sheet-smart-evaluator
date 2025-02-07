def evaluate_responses(questions, correct_answers):
  total_marks = 0
  correct = incorrect = unattempted = 0

  # Subject-wise scoring (Physics, Chemistry, Mathematics)
  subject_scores = {"Physics": 0, "Chemistry": 0, "Mathematics": 0}
  subject_questions = {"Physics": {"correct": 0, "incorrect": 0, "unattempted": 0},
                       "Chemistry": {"correct": 0, "incorrect": 0, "unattempted": 0},
                       "Mathematics": {"correct": 0, "incorrect": 0, "unattempted": 0}}

  for q in questions:
      q_id = q["question_id"]
      q_type = q["question_type"]
      subject = q["subject"]

      if q_type == "MCQ":
          chosen_option = q["chosen_option"]
          if chosen_option == "--":
              unattempted += 1
              subject_questions[subject]["unattempted"] += 1
              continue

          chosen_option_id = q["option_ids"][int(chosen_option) - 1]
          if correct_answers.get(q_id) == chosen_option_id:
              correct += 1
              total_marks += 4
              subject_scores[subject] += 4
              subject_questions[subject]["correct"] += 1
          else:
              incorrect += 1
              total_marks -= 1
              subject_scores[subject] -= 1
              subject_questions[subject]["incorrect"] += 1

      elif q_type == "SA":
          given_answer = q["given_answer"]
          if given_answer == "--":
              unattempted += 1
              subject_questions[subject]["unattempted"] += 1
              continue

          if correct_answers.get(q_id) == given_answer:
              correct += 1
              total_marks += 4
              subject_scores[subject] += 4
              subject_questions[subject]["correct"] += 1
          else:
              incorrect += 1
              total_marks-=1
              subject_scores[subject] -= 1
              subject_questions[subject]["incorrect"] += 1

  return {
      "total_marks": total_marks,
      "correct": correct,
      "incorrect": incorrect,
      "unattempted": unattempted,
      "subject_scores": subject_scores,
      "subject_questions": subject_questions
  }
