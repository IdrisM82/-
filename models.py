from django.db import models

class RequestHistory(models.Model):
    ip_address = models.GenericIPAddressField()
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)  
    method = models.CharField(max_length=10)
    user_agent = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.method} request to {self.url} from {self.ip_address} at {self.timestamp}"