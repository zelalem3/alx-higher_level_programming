const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Successfully wrote "${content}" to ${filePath}`);
  }
});
