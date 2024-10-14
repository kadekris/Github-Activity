import requests
import datetime

def get_github_user_activity(username):
    # Endpoint API GitHub untuk events pengguna
    url = f"https://api.github.com/users/{username}/events/public"
    
    # Mengirim permintaan GET ke API GitHub
    response = requests.get(url)
    
    if response.status_code == 200:
        events = response.json()
        print(f"Total events received: {len(events)}")
        return events
    elif response.status_code == 404:
        print(f"Error: Username '{username}' tidak ditemukan.")
        return None
    else:
        print(f"Error: Tidak dapat mengambil data. Kode status: {response.status_code}")
        return None

def display_user_activity(username, events):
    print(f"\nAktivitas GitHub untuk pengguna: {username}")
    print("-" * 40)
    
    if not events:
        print("Tidak ada event yang ditemukan untuk pengguna tersebut.")
        return
    # Menampilkan 10 event terbaru
    for event in events[:10]:
        event_type = event['type']
        repo_name = event['repo']['name']
        created_at = datetime.datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = created_at.strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"Event: {event_type}")
        print(f"Repository: {repo_name}")
        print(f"Tanggal: {formatted_date}")
        print("-" * 40)

def main():
    username = input("Masukkan nama pengguna GitHub: ")
    events = get_github_user_activity(username)
    
    if events:
        display_user_activity(username, events)

if __name__ == "__main__":
    main()
