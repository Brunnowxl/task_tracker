#!/bin/python3

import json
from datetime import datetime
import sys

# read data json
with open("arqJSON.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

def menu(inputs):

    id = dados["id"]+1
    if len(inputs) < 2: return None

    match inputs[1]:
        case "add":
            add(id)
        case "update":
            update()
        case "delete":
            delete()
        case "mark-in-progress":
            mark_in_progress()
        case "mark-done":
            mark_done()
        case "list":
            if len(inputs) < 3:
                list_all()
            elif inputs[2] == "done":
                list_done()
            elif inputs[2] == "todo":
                list_todo()
            elif inputs[2] == "in-progress":
                list_in_progress()
        case _:
            return None

def add(id):
    dados["tasks"][str(id)] = {"id":id,
                               "description":inputs[2],
                               "status":"todo",
                               "createdAt":str(datetime.now())}
    dados["id"] = id
    print(f"Task added sucessfully (ID: {id})")

def update():
    dados["tasks"][inputs[2]]["description"]=inputs[3]
    dados["tasks"][inputs[2]]["updateAt"]=str(datetime.now())

def delete():
    del dados["tasks"][inputs[2]]

def mark_in_progress():
    dados["tasks"][inputs[2]]["status"]="in-progress"

def mark_done():
    dados["tasks"][inputs[2]]["status"] = "done"

def list_all():
    for task in dados["tasks"].values():
        for key,value in task.items():
            print(key, ":", value)
        print()

def list_done():
    for task in dados["tasks"].values():
        if task["status"] == "done":
            for key,value in task.items():
                print(key, ":", value)
            print()

def list_todo():
    for task in dados["tasks"].values():
        if task["status"] == "todo":
            for key,value in task.items():
                print(key, ":", value)
            print()

def list_in_progress():
    for task in dados["tasks"].values():
        if task["status"] == "in-progress":
            for key,value in task.items():
                print(key, ":", value)
            print()

inputs = sys.argv
menu(inputs)


# write dado json
with open("arqJSON.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
