import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { requestAPI } from './request';

/**
 * Initialization data for the jupyterhub-gridlook extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterhub-gridlook:plugin',
  description: 'A JupyterLab extension.',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension jupyterhub-gridlook is activated!');

    requestAPI<any>('hello', app.serviceManager.serverSettings)
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `The jupyterhub_gridlook server extension appears to be missing.\n${reason}`
        );
      });
  }
};

export default plugin;
