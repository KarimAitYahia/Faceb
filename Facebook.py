import facebook

# استبدل هذه القيم بالقيم الخاصة بك
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
PAGE_ID = 'YOUR_PAGE_ID'

# تهيئة الاتصال
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN)

def reply_to_comments(post_id, message):
    comments = graph.get_connections(post_id, 'comments')
    for comment in comments['data']:
        graph.put_object(parent_object=comment['id'], connection_name='comments', message=message)

# استبدل 'POST_ID' بمعرف المنشور الذي تريد الرد عليه
reply_to_comments('POST_ID', 'شكراً لتعليقك!')
