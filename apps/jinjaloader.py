import tornado.web
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

class TemplateRendering(object):
  """
  A simple class to hold methods for rendering templates.
  """
  def render_template(self, template_name, **kwargs):
    template_dirs = []
    if self.settings.get('template_path', ''):
      template_dirs.append(self.settings['template_path'])
    env = Environment(loader=FileSystemLoader(template_dirs))

    try:
      template = env.get_template(template_name)
    except TemplateNotFound:
      raise TemplateNotFound(template_name)
    content = template.render(kwargs)
    return content

class BaseHandler(tornado.web.RequestHandler, TemplateRendering):
  """
  Tornado RequestHandler subclass.
  """
  def initialize(self):
    pass

  def get_current_user(self):
    username = self.get_secure_cookie('username')
    return username if username else None

  def render_html(self, template_name, **kwargs):
    kwargs.update({
      'settings': self.settings,
      'static_path': '/static/',
      'static_url': self.settings.get('static_url_prefix', '/static/'),
      'request': self.request,
      'current_user': self.current_user,
      'xsrf_token': self.xsrf_token,
      'xsrf_form_html': self.xsrf_form_html
    })
    content = self.render_template(template_name, **kwargs)
    self.write(content)