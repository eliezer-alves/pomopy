from flask import Flask, render_template, request, redirect, session, flash

class Controller:
    def __init__(self) -> None:
        self._request = request
        self._redirect = redirect
        self._render_template = render_template
        self._session = session
        self._flash = flash