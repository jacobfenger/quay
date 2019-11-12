"""update queue item table indices

Revision ID: f5167870dd66
Revises: 45fd8b9869d4
Create Date: 2016-12-08 17:26:20.333846

"""

# revision identifiers, used by Alembic.
revision = 'f5167870dd66'
down_revision = '45fd8b9869d4'

from alembic import op as original_op
from data.migrations.progress import ProgressWrapper
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('queueitem_processing_expires_available', 'queueitem', ['processing_expires', 'available'], unique=False)
    op.create_index('queueitem_pe_aafter_qname_rremaining_available', 'queueitem', ['processing_expires', 'available_after', 'queue_name', 'retries_remaining', 'available'], unique=False)
    op.create_index('queueitem_pexpires_aafter_rremaining_available', 'queueitem', ['processing_expires', 'available_after', 'retries_remaining', 'available'], unique=False)
    op.create_index('queueitem_processing_expires_queue_name_available', 'queueitem', ['processing_expires', 'queue_name', 'available'], unique=False)
    op.drop_index('queueitem_available', table_name='queueitem')
    op.drop_index('queueitem_available_after', table_name='queueitem')
    op.drop_index('queueitem_processing_expires', table_name='queueitem')
    op.drop_index('queueitem_retries_remaining', table_name='queueitem')
    ### end Alembic commands ###


def downgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('queueitem_retries_remaining', 'queueitem', ['retries_remaining'], unique=False)
    op.create_index('queueitem_processing_expires', 'queueitem', ['processing_expires'], unique=False)
    op.create_index('queueitem_available_after', 'queueitem', ['available_after'], unique=False)
    op.create_index('queueitem_available', 'queueitem', ['available'], unique=False)
    op.drop_index('queueitem_processing_expires_queue_name_available', table_name='queueitem')
    op.drop_index('queueitem_pexpires_aafter_rremaining_available', table_name='queueitem')
    op.drop_index('queueitem_pe_aafter_qname_rremaining_available', table_name='queueitem')
    op.drop_index('queueitem_processing_expires_available', table_name='queueitem')
    ### end Alembic commands ###
