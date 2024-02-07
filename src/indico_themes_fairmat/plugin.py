import os

from indico.core import signals
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint
from indico.modules.events.layout.util import ConferenceTheme
# from indico.web.views import WPBase

from flask_pluginengine import render_plugin_template

THEMES = [
    ConferenceTheme(name="fairmat", css_path="css/fairmat.css", title="Fairmat"),
]


class FairmatThemesPlugin(IndicoPlugin):
    """Fairmat Themes
    Provides event themes for Fairmat events.
    """

    def init(self):
        super().init()

        # self.inject_bundle("main.js", WPBase)
        # self.inject_bundle("main.css", WPBase)
        self.template_hook("html-head", self._inject_css)

        self.connect(signals.plugin.get_conference_themes, self._get_themes)
        self.connect(
            signals.plugin.get_template_customization_paths,
            self._get_customization_path,
        )

    def get_blueprints(self):
        return IndicoPluginBlueprint(self.name, __name__)

    def _get_themes(self, sender, **kwargs):
        for v in THEMES:
            yield v
        return

    def _get_customization_path(self, sender, **kwargs):
        return os.path.join(self.root_path, "templates")

    def _inject_css(self):
        return render_plugin_template("html-head.html")
