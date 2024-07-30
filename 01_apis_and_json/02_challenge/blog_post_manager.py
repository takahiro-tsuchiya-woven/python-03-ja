import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/posts"


def list_posts():
    response = requests.get(API_URL)
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception("GET request to server failed")


def create_post(new_post):
    response = requests.post(API_URL, new_post)
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception("POST request to server failed")


def update_post(post_id, new_title, new_body):
    new_data = {}
    if new_title != "":
        new_data["title"] = new_title
    if new_body != "":
        new_data["body"] = new_body

    response = requests.put(API_URL + f"/{post_id}", new_data)
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception("PUT request to server failed")


def delete_post(post_id):
    response = requests.delete(API_URL + f"/{post_id}")

    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception("DELETE request to server failed")
    

def main():
    while True:
        print("\nWelcome to blog CLI")
        print("/? for help\n")
        userCommand = input(">>> ").strip().lower()

        match userCommand:
            case "/?":
                print(
                    "Commands:\n"
                    "/?: this help menu\n"
                    "list: list all current posts\n"
                    "new: create a new post\n"
                    "update: change an existing post title or body\n"
                    "del: delete an existing post\n"
                    "q: exit the program\n"
                )
                continue
            case "list":
                try:
                    post_data = list_posts()
                    for post in post_data:
                        print(
                            f"===\n"
                            f"{post['id']}\n"
                            f"{post['userId']}\n"
                            f"{post['title']}\n"
                            f"{post['body']}\n"
                            "\n"
                        )
                except Exception as e:
                    print(e)
                    continue
                continue
            case "new":
                new_title = input("new title? (Enter to skip) >>> ")
                new_body = input("new body? (Enter to skip) >>> ")

                new_post = {"title": new_title, "body": new_body}

                try:
                    res = create_post(new_post)
                    print(res)
                except Exception as e:
                    print(e)
                    continue

                continue

            case "update":
                id = input("post_id >>> ")
                if id == "":
                    print("please try again with a valid id")
                    continue
                new_title = input("edit title? (Enter to skip) >>> ")
                new_body = input("edit body? (Enter to skip) >>> ")

                try:
                    result = update_post(id, new_title, new_body)
                    print(result)
                except Exception as e:
                    print(e)
                    continue

                continue
            case "del":
                id = input("post (id) to delete >>> ")
                if id == "":
                    print("invalid id")
                    continue
                try:
                    result = delete_post(id)
                    print(result)
                except Exception as e:
                    print(e)
                    continue
                
                continue
            case "q":
                break
            case _:
                print("invalid command. /? for help")
                continue
    return


if __name__ == "__main__":
    main()