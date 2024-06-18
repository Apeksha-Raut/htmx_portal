# Copyright (c) 2024, apeksha  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from werkzeug import Response

class Book(Document):
	pass

@frappe.whitelist()
def ping():
    return "Pong"

@frappe.whitelist(allow_guest=True)
def add_book():
    data = frappe.form_dict
    book = frappe.new_doc("Book")
    book.name = data.get("name")
    book.author = data.get("author")
    book.insert() 

    return  get_book_list()



@frappe.whitelist(allow_guest=True)
def get_book_list():
    # Render the list of books
    rendered_books = Response(frappe.render_template("templates/includes/book_list.html", {}))

    return rendered_books