from django.db import models
from pathlib import Path
from datetime import datetime
import os
from PIL import Image
from io import BytesIO
from django.core.files import File

def name_conv_fn(ins, file):
    ext = file.split(".")[-1]
    filename = '{:%Y-%m-%d-%H-%M-%S}.{}'.format(datetime.now(), ext)
    return os.path.join('Post', filename)
class Post(models.Model):
    user = models.ForeignKey('user.User', on_delete= models.RESTRICT)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to= name_conv_fn)
    added_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    def save(self, *args, **kwargs):
        if not self.image.closed:
            img = Image.open(self.image)
            img.thumbnail((500, 500), Image.ANTIALIAS)

            tmp = BytesIO()
            img.save(tmp, 'PNG')
            self.image = File(tmp, 't.png')

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

        index_together = (
            ('user', 'added_at'),
            ('added_at', ),
        )