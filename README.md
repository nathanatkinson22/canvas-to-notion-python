# Canvas to Notion Python
## Send Canvas Assignments to a Notion Database

## Introduction

This Python script uses the Canvas API to send all assignments for your current active semester into a Notion Database.

## Installation

First, clone this repository:

`$ git clone https://github.com/nathanatkinson22/canvas-to-notion-python.git
$ cd canvas-to-notion-python`

Install the dependencies:

`$ pip install -r requirements.txt`

## Usage
You will need a Canvas API access token, which you can get by following [these instructions](https://community.canvaslms.com/t5/Student-Guide/How-do-I-manage-API-access-tokens-as-a-student/ta-p/273)

You'll also need a Notion API token, which you can [learn about here](https://developers.notion.com/docs/getting-started). And you'll need to either duplicate [this Notion database](https://five-shoemaker-cc4.notion.site/3ec12b72fae04e8fac3f0acf11a0ec2a?v=e4e57aaf189f43a0abf51fa15963c770) (open link, click Duplicate in the top left) create a Notion database set up with the following properties (property names are very important or the script won't work)

- Checkbox Property: Completed
- Title Property: Assignment Name
- Date Property: Due Date
- URL Property: Assignment Link
- Text Property: ID
- Text Property: Submission Type

After you create the database in Notion, copy the [Database ID](https://developers.notion.com/docs/getting-started#step-3-add-an-item-to-a-database) and add dashes in this pattern: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"

[Share your Notion database with your new integration in Notion](https://developers.notion.com/docs/getting-started#step-2-share-a-database-with-your-integration)
 
Create a "constants.py" file in the same folder as the canvas_to_notion.py file and add the following to that file:

API_URL = "Your school's Canvas URL (e.g., https://yourschool.instructure.com"
CANVAS_TOKEN = "Your Canvas API access token"
NOTION_TOKEN = "Your Notion API access token"
NOTION_DB_ID = "Your Notion Database ID"

Run the script and if you set up everything correctly, your database should be populated with all your Canvas assignments for the active semester with titles, links, and due dates.