from django.db import models
from django.utils import timezone

class Facturation(models.Model):
    description = models.TextField()
    facture = models.FileField(upload_to="home/factures/")
    fiche = models.ForeignKey('Fiche', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de création")
    class Meta:
        ordering = ['date']
    def __str__(self):
        return self.description
        
class Commentaire(models.Model):
    commentaires = models.TextField()
    fiche = models.ForeignKey('Fiche', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de création")
    class Meta:
        ordering = ['date']
    def __str__(self):
        return self.commentaires

class Fiche(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    age = models.IntegerField()
    GENRE_CHOICES = (
    ('HOMME', 'Homme'),
    ('FEMME', 'Femme'),
    )
    genre = models.CharField(max_length=5, choices=GENRE_CHOICES)
    telephone = models.CharField(null=True, blank=True, max_length=14)
    mail = models.EmailField(null=True, blank=True,max_length=100)
    adresse = models.TextField()
    ville = models.CharField(max_length=30)
    cp = models.CharField(max_length=5, verbose_name="Code Postale")
    paiement = models.DateTimeField(blank=True, null=True, verbose_name="Dernier Paiement")
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de création")


    class Meta:
        verbose_name = "Fiche"
        ordering = ['nom']

    def __str__(self):
        return self.nom