import requests
from canvasapi import Canvas
from pytz import timezone
import dateutil
from dateutil.parser import *
import constants

# Canvas API URL
API_URL = constants.API_URL
# Canvas API key
CANVAS_TOKEN = constants.CANVAS_TOKEN
NOTION_TOKEN = constants.NOTION_TOKEN
NOTION_DB_ID = constants.NOTION_DB_ID

canvas = Canvas(API_URL, CANVAS_TOKEN)

def main():
    # getAssignments()
    canvas_user = canvas.get_user('self')

    courses = canvas_user.get_courses(enrollment_state='active')
    for course in courses:
        assignments = course.get_assignments(include='all_dates')
        for assignment in assignments:
            a_name = f'{assignment.name}'
            due_date = dateutil.parser.parse(f'{assignment.due_at}')
            a_due_time = due_date.astimezone(timezone('America/Denver'))
            a_id = f'{assignment.id}'
            a_submission_types = f'{assignment.submission_types}'
            # a_description = f'{assignment.description}'
            a_url = f'{API_URL}/courses/{assignment.course_id}/assignments/{a_id}'
            completed = False
            createAssignments(a_name, a_due_time, a_id, a_submission_types, a_url, completed)

def getAssignments():
    get_url = f'https://api.notion.com/v1/databases/{NOTION_DB_ID}/query'

    r = requests.post(get_url, headers={
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {NOTION_TOKEN}"
    })
    result_dict = r.json()
    result_list = result_dict['results']
    print(result_list)

def createAssignments(name, due, a_id, sub_type, a_url, completed=False):
    url = "https://api.notion.com/v1/pages"

    payload = {
            "parent": {
                "type": "database_id",
                "database_id": NOTION_DB_ID
            },
            "properties": {
                'Assignment Name': {'type': 'title', 'title': [
                        {'type': 'text', 'text': {'content': name
                            }
                        }
                    ]
                },
                'Due Date': {'type': 'date', 'date': {'start': due.isoformat(), 'end': None, 'time_zone': None}
                }, 
                'Submission Type': {'type': 'rich_text', 'rich_text': [
                        {'type': 'text', 'text': {'content': sub_type
                            }
                        }
                    ]
                }, 
                'ID': {'type': 'rich_text', 'rich_text': [
                        {'type': 'text', 'text': {'content': a_id
                            }
                        }
                    ]
                },
                'Assignment Link': {'url': a_url},
                "Completed": {
                    "checkbox": completed
                }
            }
        }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {NOTION_TOKEN}"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

if __name__ == "__main__":
    main()