from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from cinp.orm_django import DjangoCInP as CInP

cinp = CInP( 'Products', '0.1' )

@cinp.model()
class Product( models.Model ):
  name = models.CharField( max_length=200 )
  cost = models.IntegerField( min_value=0, help='in howe-bucks' )
  location = models.CharField( max_length=3 )
  available = models.IntegerField( min_value=0 )
  
  updated = models.DateTimeField( editable=False, auto_now=True )
  created = models.DateTimeField( editable=False, auto_now_add=True )


  @cinp.check_auth()
  @staticmethod
  def checkAuth( user, verb, id_list, action=None ):
    return cinp.basic_auth_check( user, verb, action, Job )

  def clean( self, *args, **kwargs ):  # TODO: also need to make sure a Structure is in only one complex
    super().clean( *args, **kwargs )
    errors = {}

    if errors:
      raise ValidationError( errors )

  class Meta:
    default_permissions = ()

  def __str__( self ):
    return 'Product "{0}"'.format( self.name )


# group model
# prohipited group
# time of date group
# n-shot group
#
