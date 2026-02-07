import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.petrofac.lubrication',
  appName: 'Petrofac Lubrication',
  webDir: 'dist',
  android: {
    allowMixedContent: true,
    backgroundColor: '#0f172a'
  }
};

export default config;
