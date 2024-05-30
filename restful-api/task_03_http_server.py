#!/usr/bin/env python3
"""
Ce module implémente un serveur HTTP simple utilisant le module http.server de Python.
Il définit une classe de gestionnaire de requêtes HTTP qui répond à différentes requêtes GET.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Cette classe est un gestionnaire de requêtes HTTP qui hérite de http.server.SimpleHTTPRequestHandler.
    Elle définit une méthode do_GET pour gérer les requêtes GET.
    """

    def do_GET(self):
        """
        Cette méthode est appelée pour gérer les requêtes GET.
        Elle vérifie le chemin de la requête et renvoie une réponse appropriée.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))
