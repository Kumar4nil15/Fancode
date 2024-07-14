from utils.api_helper import get_users, get_todos

def get_fancode_users():
    users = get_users()
    fancode_users = [user for user in users if -40 <= float(user['address']['geo']['lat']) <= 5 and 5 <= float(user['address']['geo']['lng']) <= 100]
    return fancode_users

def user_completed_percentage(user_id):
    todos = get_todos()
    user_todos = [todo for todo in todos if todo['userId'] == user_id]
    if not user_todos:
        return 0
    completed_todos = [todo for todo in user_todos if todo['completed']]
    return len(completed_todos) / len(user_todos) * 100

def check_fancode_users_completion():
    fancode_users = get_fancode_users()
    result = {}
    for user in fancode_users:
        completion_percentage = user_completed_percentage(user['id'])
        result[user['name']] = completion_percentage > 50
    return result

if __name__ == "__main__":
    result = check_fancode_users_completion()
    for user, is_completed in result.items():
        print(f"{user}: {'Completed' if is_completed else 'Not Completed'} more than 50% of tasks")

