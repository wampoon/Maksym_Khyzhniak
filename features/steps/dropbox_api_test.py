from behave import *
from features.request_factory import *
import os


u = UploadRequest()
m = GetFileMetadataRequest()
d = DeleteRequest()


@given(u'file named "file.txt"')
def step_impl(context):
    assert os.path.isfile('./sample_files/file.txt')==True


@when(u'we upload file "file.txt" to Dropbox')
def step_impl(context):
    u.get_response()


@then(u'we see file "file.txt" uploaded')
def step_impl(context):
    assert u.response.status_code == 200


@given(u'file named "file.txt" is uploaded')
def step_impl(context):
    assert u.response.status_code == 200


@when(u'we request metadata of file "file.txt" by id')
def step_impl(context):
    m.get_response(u.id)


@then(u'we receive metadata for file "file.txt"')
def step_impl(context):
    assert m.response.status_code == 200


@given(u'we have absolute file path after file "file.txt" was downloaded')
def step_impl(context):
    assert m.file_path!=None


@when(u'we request to delete file "file.txt"')
def step_impl(context):
    d.get_response(m.file_path)


@then(u'we see file "file.txt" deleted')
def step_impl(context):
    assert d.response.status_code==200