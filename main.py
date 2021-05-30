#!/usr/bin/python3
"""to test to_json"""
to_json_file = __import__('to_json_string').to_json

dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}

filename = "test_file"

to_json_file(dictionary, filename)
