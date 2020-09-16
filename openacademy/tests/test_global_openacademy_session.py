# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class GlobalTestOpenAcademySession(TransactionCase):
    '''
    This create global test to sessions
    '''

    # Seudo-constructor method
    def setUp(self):
        super(GlobalTestOpenAcademySession,self).setUp()
        self.session = self.env['openacademy.session']
        self.partner_vauxoo = self.env.ref('base.res_partner_4')
        self.course = self.env.ref('openacademy.course1')
        self.partner_attendee = self.env.ref('base.res_partner_1')
    # Generic methods 
 
    # Test methods
    def test_10_instructor_is_attende(self):
        '''
        Check that raise of 'A session's instructor can't be an attendee'
        '''
        with self.assertRaisesRegexp(
            ValidationError,
            "A session's instructor can't be an attendee"
            ):
            self.session.create({
                'name': 'Session test 1',
                'seats': 1,
                'course_id': self.course.id,
                'instructor_id': self.partner_vauxoo.id,
                'attendee_ids': [(6,0,[self.partner_vauxoo.id])],

            })

    def test_20_wfk_done(self):
        '''
        Check that the workflow work fine
        '''
        self.session.create({
                'name': 'Session test 1',
                'seats': 1,
                'course_id': self.course.id,
                'instructor_id': self.partner_vauxoo.id,
                'attendee_ids': [(6,0,[self.partner_attendee.id])],

            })
       