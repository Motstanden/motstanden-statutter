# Introduksjon
Denne teksten er delt inn i to deler:
1. [Den første delen](#del-1:-veiledning-for-medlemmer) er skrevet generelt for motstandens medlemmer.
2. [Den andre delen](#del-2:-veiledning-for-vedlikeholdere) er skrevet for personer som skal gjøre endringer på statuttene. Denne seksjonen er altså ikke nødvendig å lese dersom du ikke skal gjøre endringer på kildekoden.

## Innholdsfortegnelse
* [Del 1: Veiledning for medlemmer](#del-1:-veiledning-for-medlemmer)
    * [Generelt](#generelt)
    * [Opprett en issue](#opprett-en-issue)
* [Del 2: Veiledning for vedlikeholdere](#del-2:-veiledning-for-vedlikeholdere)
    * [Arbeidsflyt](#arbeidsflyt)
    * [Retningslinjer](#retningslinjer)
        * [Språk](#språk)
        * [Branch struktur](#branch-struktur)
        * [Gjøre endringer](#gjøre-endringer)
        * [Publisere endringer](#publisere-endringer)
    * [Kom i gang – lokal redigering](#kom-i-gang-–-lokal-redigering)
        * [Installer *Tex live*](#installer-tex-live)
        * [Instaler et redigeringsprogram](#instaler-et-redigeringsprogram)
        * [Last ned og rediger](#last-ned-og-rediger.)
    * [Kom i gang – online redigering](#kom-i-gang-–-online-redigering)
        * [Overleaf](#overleaf)
            * [Importer fra github](#importer-fra-github)
            * [Publisere endringer til github](#publisere-endringer-til-github)
    * [Dokumentasjon av Latex kode](#dokumentasjon-av-latex-kode)
        * [Ny definisjon](#ny-definisjon)
        * [Ny statutt](#ny-statutt)

# Del 1: Veiledning for medlemmer

## Generelt
* Statuttene kan leses i sin helhet i filen: **statuttene.pdf**
* Endringer etter generalvorsamlinger kan finnes ved å gå inn på **Pull Requests** fanen.
* Forslag og spørsmål kan legges fram ved å gå inn på **Issues** fanen.

## Opprett en issue
Har du et forslag? Eller et spørsmål? Eller noe du vil påpeke til neste genvors? Opprett en *issue* på det! 

På *issues* kan man diskutere absolutt alt som er relatert til statuttene! Der skal det være superlav terskel for å publisere meninger, forslag, og spørsmål – når som helst! 

Åpne issues kommer automatisk til å bli diskutert på neste generalvorssamling. Ved å opprette en issue har du derfor en garanti for at din mening blir husket på og drøftet på neste generalvorssamlingen.

# Del 2: Veiledning for vedlikeholdere
## Arbeidsflyt
1. Lag ny branch
    ```
    git checkout -b genvors/vår-2021
    ```
2. Gjør endringer, commit, repeat.
    ```
    git add .
    git commit -m "Legg til definisjon av en kortsluttning"
    ```
3. Publiser branch på GitHub.
    ```
    git push -u origin genvors/høst-2021
    ```
4. Sett opp en pull request med de nye endringer i henhold til [retningslinjene](#publisere-endringer). 

## Retningslinjer

### Språk
* Alt som skrives i Latex – og ikke er en del av selve statuttene – skal skrives på engelsk. Dette gjelder blant annet kommentarer, variabelnavn, funksjonsnavn, miljønavn osv. 
* Alt annet skal skrives på norsk.

### Branch struktur
Alle endringer skal skje på brancher. Navnekonvensjon for en branch er *<kategori\>/\<kort-beskrivelse\>*. Kategorien som velges skal være èn av følgende:

* **genvors** -> `git checkout -b genvors/høst-2021`
    * Alle endringer som har blitt vedtatt på generalvorssamlingen.
* **redaksjon** -> `git checkout -b redaksjon/fiks-skrivefeil`
    * Redaksjonelle endringer i statuttene. 
    * Redaksjonelle endringer defineres som tekstendringer som ikke endrer mening eller budskap. For eksempel fiksing av skrivefeil og grammatikk.
* **forslag** -> `git checkout -b forslag/endre-medlem-definisjon`
    * Forslag til endringer i statuttene som skal tas opp på neste genvors.
* **kode** ->  `git checkout -b kode/større-font`
    * Alle endringer som ikke endrer selve statuttene.

### Gjøre endringer
Alle har lov til å gjøre endringer (på en ny branch) og sette opp en pull request. Endringene kan være hva som helst, men det er ingen garanti for at pull requesten blir akseptert. Les videre for å få bedre oversikt over dette.

### Publisere endringer
* Alle endringer skal gjøre med Pull Requests. 
    * Endringer etter generalvorssamling skal ligge ute åpenlyst for alle medlemmer i 14 dager før pull requesten kan merges til master.
    * Redaksjonelle endringer skal godkjennes av styret. 
    * forslag godkjennes ikke før de har blitt vedtatt på generalvorssamling.
    * Endringer i kode godkjennes av webansvarlig i styret.

## Kom i gang – lokal redigering

### Installer *Tex live*
*[Tex live](https://www.tug.org/texlive/)* er en *"latex distribution"*. En latex distribusjon er kort fortalt en samling med programvare som er nødvendig for å kompilere *.tex* filer. Det fins mange latex distribusjoner, men i dette prosjektet bruker vi Tex Live. Tex Live er den mest annerkjente distribusjonen, og er (per 2021) sett på som de facto standard.

Ved å bruke Tex Live sikrer vi at alle jobber i likt miljø. Dermed risikerer man ikke å 'breake' `.tex` filene for andre som jobber på prosjektet. Dersom du er **latex wizzard**, og har fullstendig peiling på hva du holder på med, kan du velge en annen distribusjon.  

Last ned Tex Live [her](https://www.tug.org/texlive/acquire-netinstall.html).

### Instaler et redigeringsprogram
Det fins flere redigeringsprogram for latex, så her står man fritt til å velge hva som helst. Det mest omfattende programmet (per 2021) er **[TeXstudio](https://www.texstudio.org/)**. Det er et åpent kildekodeprosjekt i [aktiv utvikling](https://github.com/texstudio-org/texstudio), og er det programmet med mest tillegsfunksjoner.

Det er verdt å få med seg at redigeringsprogrammer for latex hovedsakelig er tekstredigeringsverktøy som kaller på API-er i latex distribusjonen du har installert. Under panseret gjør altså latex distribusjonen det meste av arbeidet. Derfor kan ikke et redigeringsprogram stå på egne ben. En latex distribusjon må først være instalert på opperativsystemet.

### Last ned og rediger.
Gratulerer, nå gjenstår det bare å laste ned prosjektet, åpne `statutter.tex`, og å starte å rediger.  

## Kom i gang – online redigering
Det fins flere måter å redigere latex dokumenter i nettlerse på, men *[overleaf](https://www.overleaf.com/)* er den desidert mest brukte og mest populære (per 2021). *Overleaf* koster egentlig penger, men det er gratis dersom man registrerer seg med student–e-posten. 

### Overleaf
#### Importer fra github
Dette gjør du ved å klikke på **New Project > Import from GitHub** (se bildet under). Etter dette må du godta at *overleaf* kan koble seg til github brukeren din.

<img src="ReadmeImages\OverleafImportFromGithub.png" height="200"/>

Du er nå klar for å starte å redigere statuttene.

#### Publisere endringer til github

1. **Sørg for at ALLE feilmeldinger er fikset** (se bildet under). **Det er strengt forbudt å publisere .tex filer med feilmeldinger til github!!** Feilmeldinger vil gjøre at .tex filene ikke kan bli kompilert lokalt på datamaskiner. Uhåndterte feilmeldinger vil derfor ødelege for andre.

    <img src="ReadmeImages\OverleafWarnings.png" height="100"/>

2. Last ned de 'gamle statuttene'.
    ``` 
    git clone https://github.com/Motstanden/statutter.git
    ```
4. Last ned kildekodefilene fra *Overleaf* ved å klikke på: *Menu > Download > Source*.
3. Klikk på recompile og last ned pdf versjonen.
5. Kopier kildekodefilene og pdf dokumentet inn i mappen med de 'gamle statuttene'. Sørg for at de nye filene overskriver de gamle filene.
7. Lag ny branch og legg til endringene.
    ```
    git checkout -b redaksjon/fiks-skrivefeil
    git add .
    git commit -m "Fiks diverse skrivefeil i statuttene"
    ```
6. Publiser til *GitHub*
    ```
    git push -u origin redaksjon/fiks-skrivefeil
    ```
7. Sett opp en pull request til master på *GitHub*.

## Dokumentasjon av Latex kode
### Ny definisjon
Det er laget et egendefinert miljø for definsjoner (punktene i seksjon 1). Syntaksen for miljøet er:

    ```
    \begin{definition}[\label{her-kan-du-legge-in-et-label}]
        Her skriver du selve definisjonen....
    \end{definition}
    ```
Latex vil automatisk håndtere formatering og plassering.
For å finne definisjonen av miljøet, se etter: `\newenvironment{definition}`

### Ny statutt
Det er laget et egendefinert miljø statutter (alle punkter som ikke er definisjoner). Syntaksen er identisk som definisjon miljøet:

    ```
    \begin{statute}[\label{her-kan-du-legge-in-et-label}]
        Her skriver du inn den nye statutten som ble vedtatt på genvors...
    \end{statute}
    ```
Akkuratt som definition miljøet, vil latex automatisk håndtere formatering og plassering. For å finne definisjonen av miljøet, se etter: `\newenvironment{statute}`