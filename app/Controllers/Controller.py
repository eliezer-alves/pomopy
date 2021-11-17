from flask import Flask, render_template, request, redirect, session, flash, jsonify
from datetime import datetime

class Controller:
    def __init__(self) -> None:
        self._request = request
        self._redirect = redirect
        self._render_template = render_template
        self._session = session
        self._flash = flash
        self._jsonify = jsonify
        self.datetime = datetime