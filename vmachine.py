import requests
import json

url = "https://management.azure.com/subscriptions/f0dd45d3-896e-4f29-9ca0-df14c83d6ddc/resourceGroups/lab4/providers/Microsoft.Network/publicIPAddresses/ipv4?api-version=2023-05-01"

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzU4NTE1ZWUyLWEzY2UtNDM0NC1iMmUxLTY4ODJmZDY5MTkwMS8iLCJpYXQiOjE3MDAxNTQ3NzAsIm5iZiI6MTcwMDE1NDc3MCwiZXhwIjoxNzAwMTYwMTgyLCJhY3IiOiIxIiwiYWlvIjoiQVdRQW0vOFZBQUFBR2tGSm1rR3hBRUhjTXBETUVaeWQyMzJyZFcxdFpZZVZubWZLejFTektGS1U2dHAvc09WU2h0OWNXakwxa2pZY3pwMTVaQ0RPeWpxUVNTWHhDWHY1bCtiNlNISkpkY2xlSWkxbHB2Zy8vNVRocjcvUkZ6NlJ1MlhnaVk2Qk9DVnAiLCJhbHRzZWNpZCI6IjE6bGl2ZS5jb206MDAwMzQwMDEzNUU1RjY4MSIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJlbWFpbCI6ImNoaWR1YmVtYW1lY2hpMkBnbWFpbC5jb20iLCJmYW1pbHlfbmFtZSI6IkFNRUNISSIsImdpdmVuX25hbWUiOiJDSElEVUJFTSIsImdyb3VwcyI6WyIxM2Q5MWZhNy0zZWQ1LTRhNzUtYWMxZS0yYzY5NjE0ZGI0NDkiXSwiaWRwIjoibGl2ZS5jb20iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxNDcuMjUyLjE5LjIxNyIsIm5hbWUiOiJDSElEVUJFTSBBTUVDSEkiLCJvaWQiOiI0NjFmMjIyZi01MjM5LTRlNjQtOTE4NC1hYzhiMzg2ZDZkOWEiLCJwdWlkIjoiMTAwMzIwMDMwRjAzRjY2NCIsInJoIjoiMC5BYThBNGw1UldNNmpSRU95NFdpQ19Xa1pBVVpJZjNrQXV0ZFB1a1Bhd2ZqMk1CT3ZBRGcuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiRi00dU1qM3NNWjIxYzk1MzV5dzFsbVozbm1MUUxJTHJvQ1hfb3FZTTNaRSIsInRpZCI6IjU4NTE1ZWUyLWEzY2UtNDM0NC1iMmUxLTY4ODJmZDY5MTkwMSIsInVuaXF1ZV9uYW1lIjoibGl2ZS5jb20jY2hpZHViZW1hbWVjaGkyQGdtYWlsLmNvbSIsInV0aSI6IjlWUWhDTzFCMGtHazBBQTVCWFlPQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjYyZTkwMzk0LTY5ZjUtNDIzNy05MTkwLTAxMjE3NzE0NWUxMCIsImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfY2FlIjoiMSIsInhtc190Y2R0IjoxNjk5MTE4MzEwfQ.YSHR5cU4spOfny5F1VYCOU2M0bnsFvRxjYbdmDVnuQ7n--_oxNlomtxo4WRxmDS8taU59QVKHVUhqozdgaMoN7WS-U5ZOxcxoPEX5pkFxgcbTorfSRYDp88MJFS4TuI2NDxmhNCWj6j6LD2EF12uxKGz9wTb29JyHXTgeMBpX9TR9EsEgu2WImaJiOf2cVZOcZQqy5pfty-flQKbpIQB-Cc6zCURfr3zRYMkUfKfIl68Vbi1i3-dlwc41po8-I0yeHhYrAEccGMi2j6GRLmhrv_vr4edXC-QXIOkQvRgjg4flQ8ugSHChjLp_kb6LLg26HIpIV1Tdnwy9Uh_u2UJYQ',
    'Content-type': 'application/json'
}

data = {
    
  "id": "/subscriptions/f0dd45d3-896e-4f29-9ca0-df14c83d6ddc/resourceGroups/lab4/ providers/Microsoft.Compute/virtualMachines/vm4",
  "type": "Microsoft.Compute/virtualMachines",
  "properties": {
    "osProfile": {
      "adminUsername": "chidubemamechi2@gmail.com",
      "secrets": [
        
      ],
      "computerName": "vm4",
      "linuxConfiguration": {
        "ssh": {
          "publicKeys": [
            {
              "path": "/home/chidubemamechi2@gmail.com/.ssh/authorized_keys",
              "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDJM/Y+UJRjx1Z7TcW0t8PB0OysIfq5G7HcyPBak7nIgsm8pNFfMkfj00jyUiok7WA4cShmY4wSDPoMz311y4p7bcAck7C2EOgwtdjqXAmuK+slZQpOqAcHfBPt64WvDLFBqTseMW6ofdYaUwif0doEgoI/qBUt6mMBMIRbkYEQFAs1yo4J+pnA/0poz1UmwQkyJ1om9/yZ44+BSJMb39An7QPQTuatQF5svZL221c8dUNfPIEaLKx+k7WPhF3Nu3XZkEmuKKDsyKIInlCPJXNHdAfhGgqNwj2g6LYAgkTa8eMIAs63p6safDGIjlCX37QE0fMfVaBf0cIHc1jV093IeLnLv6JCAdGovm5ZuuFyljgoTwSL3DCJh5fzWaaF6d/zB4RPh95KoK6AtTKuPPHUIqi57NaWR+04qzpffgfG98KosmCgIZysfWwZmYr/ex/K65dp0xTf/+xmc9DxJTgXbX3RTl1Fp4xi+eujbWnEKVXthKaz+zc+6jV+3I38ANE= chidubemamechi2@gmail.com@chidubem"
            }
          ]
        },
        "disablePasswordAuthentication": true
      }
    },
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/f0dd45d3-896e-4f29-9ca0-df14c83d6ddc/resourceGroups/lab4/ providers/Microsoft.Network/networkInterfaces/nic4",
          "properties": {
            "primary": true
          }
        }
      ]
    },
    "storageProfile": {
      "imageReference": {
        "sku": "20.04-LTS",
        "publisher": "Canonical",
        "version": "latest",
        "offer": "UbuntuServer"
      },
      "dataDisks": [
        
      ]
    },
    "hardwareProfile": {
      "vmSize": "Standard_D1_v2"
    },
    "provisioningState": "Creating"
  },
  "name": "vm4",
  "location": "northeurope"

}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
