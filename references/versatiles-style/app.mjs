import { styles } from '@versatiles/style';
import fs from 'fs';

let style_colorful = styles.colorful({
  // languageSuffix: 'de', or en
});

let style_guess = styles.guessStyle({
  // languageSuffix: 'de', or en
});
 


let style_eclipse = styles.eclipse({
  languageSuffix: 'en',
});


let style_neutrino = styles.neutrino({
  languageSuffix: 'en',
});

let style_graybeard = styles.graybeard({
  languageSuffix: 'en',
});

fs.writeFileSync('style_colorful.json', JSON.stringify(style_colorful));
fs.writeFileSync('style_guess.json', JSON.stringify(style_guess));

fs.writeFileSync('style_eclipse.json', JSON.stringify(style_eclipse));
fs.writeFileSync('style_neutrino.json', JSON.stringify(style_neutrino));
fs.writeFileSync('style_graybeard.json', JSON.stringify(style_graybeard));