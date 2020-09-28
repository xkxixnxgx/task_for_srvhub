from webapp import create_app
from webapp.model import db
from webapp.comment.models import Comment

app = create_app()

with app.app_context():
    comment = input('Введите комментарий к изображению: ')
    picture_id = input('Введите id изображения: ')

    new_comment = Comment(comment=comment, picture_id=picture_id)

    db.session.add(new_comment)
    db.session.commit()
    print('Comment with id {} added'.format(new_comment.id))
