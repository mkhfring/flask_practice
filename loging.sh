#!/bin/bash
curl -X POST http://127.0.0.1:5000/login \
     -H "Content-Type: application/json" \
     -d '{"username": "example", "password": "123456"}'
