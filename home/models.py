from django.db import models

class Villes(models.Model):
    ville = models.CharField(blank=False,max_length=30, unique=True)
    cp = models.CharField(blank=False,null=False,max_length=5, verbose_name="Code Postale")
    deliveroo = models.BooleanField(default=False)
    ubereat = models.BooleanField(default=False,verbose_name="Uber Eat")
    justeat = models.BooleanField(default=False,verbose_name="Just Eat")
    monoprix = models.BooleanField(default=False)
    houra = models.BooleanField(default=False)
    carrefour = models.BooleanField(default=False)
    auchan = models.BooleanField(default=False)
    intermarche = models.BooleanField(default=False)
    ovs = models.BooleanField(default=False)
    youpijob = models.BooleanField(default=False)
    jemepropose = models.BooleanField(default=False)
    allovoisin = models.BooleanField(default=False)
    shiva = models.BooleanField(default=False)
    maisonetservices = models.BooleanField(default=False)
    helpling = models.BooleanField(default=False)
    o2 = models.BooleanField(default=False)
    vitalliance = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Ville'
        ordering = ['ville']
    def __str__(self):
        return self.ville