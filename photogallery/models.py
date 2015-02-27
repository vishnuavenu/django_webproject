from PIL import Image
from django.db import models
from django.db.models.fields.files import ImageField, ImageFieldFile
from django.template.defaultfilters import slugify
import os
from django.db.models import permalink

# Helper class for Thumbnailing 



class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    
    thumbpath = property(_get_thumb_path)
    
    def _get_thumb_url(self):
        return _add_thumb(self.url)
    
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        print "-----------------------------------------------------------------"
        print "its invoked!", self.path, "\n+++++++++++++++++++++++++++++++"
        print self.thumbpath
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)
        img.thumbnail(
                      (self.field.thumb_width, self.field.thumb_height),
                      Image.ANTIALIAS
                      )
        img.save(self.thumbpath, 'JPEG')
        
    def delete(self, save=True):
        if os.path.exists(self.thumbpath):
            os.remove(self.thumbpath)
        super(ThumbnailImageFieldFile, self).delete(save)
    

class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile 
    
    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)
        

        
# main Class Started


class Category(models.Model):
    cat_name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
   
    
    class Meta:
        ordering = ['cat_name']
        
    def __unicode__(self):
        return self.cat_name
    
    
    
class Photo(models.Model):
    item = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to="photogallery")
    caption = models.CharField(max_length=250, blank=True)
    
    ''' 
    def save(self, *args, **kwargs):
        
        return (Photo, self).save(*args, **kwargs)
    '''
    class Meta:
        ordering = ['title', 'image']
        
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'object_id':self.id})
        
def _add_thumb(s):
    parts= s.split('.')
    parts.insert(-1, "thumb")
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)


    
    
    
        