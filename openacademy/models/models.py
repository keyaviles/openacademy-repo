# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Clase o modelo para definir cursos'

    name = fields.Char(string="Title",required=True)
    description=fields.Text()
    responsable_id=fields.Many2one(
        'res.users',string="Responsible",
        index=True,ondelete='set null')
    sessions_ids=fields.One2many('openacademy.session','course_id')

class Session(models.Model):
    _name = 'openacademy.session'
    _description='Clase o modelo para definir sesiones'

    name=fields.Char(required=True)
    start_date=fields.Date()
    duration=fields.Float(digits=(6,2),help="Duration in days")
    seats=fields.Integer(string="Number of seats")
    instructor_id=fields.Many2one('res.partner','Instructor')
    course_id=fields.Many2one('openacademy.course',ondelete='cascade',
                                string="Course", required=True)
    attendee_ids=fields.Many2many('res.partner',string="Attendees")
    
   
