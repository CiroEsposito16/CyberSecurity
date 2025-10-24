Soft reset (consigliato per primo tentativo)
# 1) Chiudi VS Code se aperto
killall code 2>/dev/null || true
# 2) Backup e azzeramento impostazioni utente/estensioni/cache
mv ~/.config/Code ~/.config/Code.bak.$(date +%s)
mv ~/.vscode ~/.vscode.bak.$(date +%s)
rm -rf ~/.cache/Code
# 3) Avvia pulito (senza estensioni)
code --disable-extensions
Reset totale (purge + reinstall)
# 1) Chiudi VS Code
killall code 2>/dev/null || true
# 2) Rimuovi completamente il pacchetto
sudo apt purge -y code
sudo apt autoremove -y
# 3) Pulisci repo vecchio (se presente)
sudo rm -f /etc/apt/sources.list.d/vscode.list
sudo rm -f /etc/apt/keyrings/packages.microsoft.gpg
sudo install -d -m 0755 /etc/apt/keyrings
# 4) Reinstalla la chiave e il repository ufficiale Microsoft
wget -qO- https://packages.microsoft.com/keys/microsoft.asc \
| gpg --dearmor | sudo tee /etc/apt/keyrings/packages.microsoft.gpg >/dev/null
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" \
| sudo tee /etc/apt/sources.list.d/vscode.list >/dev/null
# 5) Aggiorna e reinstalla VS Code
sudo apt update
sudo apt install -y code
# 6) Primo avvio pulito (senza estensioni)
code --disable-extensions
(Opzionale) Reinstalla le estensioni essenziali
# Python e Jupyter
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
(Opzionale) Imposta esplicitamente la shell del terminale integrato
# Zsh e Bash su Kali
echo '{
  "terminal.integrated.defaultProfile.linux": "zsh",
  "terminal.integrated.profiles.linux": {
    "zsh":  { "path": "/usr/bin/zsh" },
    "bash": { "path": "/bin/bash" }
  }
}' > ~/.config/Code/User/settings.json
Se dopo il soft reset il terminale resta “muto”, esegui direttamente il reset totale.