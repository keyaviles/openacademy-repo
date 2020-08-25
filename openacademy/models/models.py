# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


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
    #datetime_test=fields.Datetime(default=time.strftime('%Y-%m-%d %H:%M:%S'))
    duration=fields.Float(digits=(6,2),help="Duration in days")
    seats=fields.Integer(string="Number of seats")
    instructor_id=fields.Many2one('res.partner','Instructor',domain=['|',('instructor','=','True'),('category_id.name','ilike','Teacher')])
    course_id=fields.Many2one('openacademy.course',ondelete='cascade',
                                string="Course", required=True)
    attendee_ids=fields.Many2many('res.partner',string="Attendees")
    taken_seats=fields.Float(compute='_taken_seats')

    @api.depends('seats','attendee_ids')
    def _taken_seats(self):
        import pdb; pdb.set_trace()
        #for record in self.filtered(lambda r: r.seats != 0):
        for record in self.filtered(lambda r: r.seats):
            record.taken_seats= 100.0 * len(record.attendee_ids) / record.seats