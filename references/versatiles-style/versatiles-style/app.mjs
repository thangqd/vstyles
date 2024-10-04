import fs from 'fs';
import { styles } from '@versatiles/style';

let style = styles.colorful({
  languageSuffix: '_en',
});

let styleJSON = JSON.stringify(style, null, 2);

fs.writeFileSync('style.json', styleJSON);

console.log('style.json file has been created successfully.');
