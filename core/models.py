from django.db import models

# Create your models here.


class Deals(models.Model):
    customer = models.CharField("Customer", max_length=255)
    item = models.CharField("Item", max_length=255)
    total = models.PositiveSmallIntegerField("Total")
    quantity = models.PositiveSmallIntegerField("Quantity")
    date = models.DateTimeField("Date")

    class Meta:
        verbose_name = "Deals"
        verbose_name_plural = "Deals"
        # ordering = ("-total",)

    def __str__(self) -> str:
        return self.customer


class CSVFiles(models.Model):
    csv_file = models.FileField("CSV file", upload_to="csv_files/")
    time = models.DateTimeField("Date", auto_now_add=True)

    class Meta:
        verbose_name = "CSV file"
        verbose_name_plural = "CSV files"
