# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT

class TrainLesson(models.Model):
    _name = 'pscloud.train.lesson'
    _description = "课程信息"
    ####fields start######
    name = fields.Char(string='Name')
    teacher_id = fields.Many2one('res.partner', string='老师', domain=[('is_teacher', '=', True)])
    student_ids = fields.Many2many('res.partner', string='学生', domain=[('is_student', '=', True)], readonly=True)
    start_date = fields.Date(string='开始时间')
    end_date = fields.Date(string='结束时间')
    continue_days = fields.Integer(string='持续天数', compute='_compute_days', store=True)
    state = fields.Selection([
        ('draft', '草稿'),
        ('confirm', '确认'),
        ], string='状态', readonly=True, copy=False, index=True, default='draft')
    seat_qty = fields.Integer(string='座位数')
    subject_id = fields.Many2one('pscloud.training.subject', string='科目')
    person_id = fields.Many2one('res.partner', related='subject_id.person_id', readonly=True)
    desc = fields.Text(string='描述')


######科目
class TrainingSubject(models.Model):
    _name = 'pscloud.training.subject'
    _description = "科目"

    name = fields.Char(string='名称')
    person_id = fields.Many2one('res.partner', string='负责人')
    lesson_ids = fields.One2many('pscloud.training.lesson', 'subject_id', string='课程')
    desc = fields.Text(string='描述')
