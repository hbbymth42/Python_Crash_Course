from operator import itemgetter
import requests
import plotly.express as px

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    try:
        r = requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()

        # Build a dictionary for each article.
        submission_dict = {
            'by': response_dict['by'],
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        print("Promotional Post")
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)
submission_links, num_comments, hover_texts = [], [], []
for submission_dict in submission_dicts:
    submission_link = f"<a href='{submission_dict['hn_link']}'>"
    submission_link += f"{submission_dict['title']}</a>"
    hover_text = f"{submission_dict['title']}<br /> by {submission_dict['by']}"
    submission_links.append(submission_link)
    num_comments.append(submission_dict['comments'])
    hover_texts.append(hover_text)

title = "Most Active Discussions on Hacker News"
labels = {'x': 'Submission', 'y': 'Number of Comments'}
fig = px.bar(x=submission_links, y=num_comments, title=title, labels=labels,
             hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()