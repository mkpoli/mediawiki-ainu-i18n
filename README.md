# mediawiki-ainu-i18n

## Introduction

### English
This is a Mediawiki translation project to Ainu language. Because translatewiki is not available for Ainu language now, and the fact it requires a long time to even register and apparently more difficult to approve a language. We have to use another way to translate here in Github by writing in raw JSON for now.

There `ain.json` file is based on `ja.json` with some Ainu translations. The `ja.json` and `en.json` file i18n files located in `mediawiki-1.41.0/languages/i18n` directory in the distributed Mediawiki package. See those files for the original author.

There are also localization files in the extension directory, which are having a similar file structure of `ain.json`, `ja.json`, and `en.json` for each extension. The latter two are also located in each extension's distributed package. See those files for the original author. There are also a `metadata.json` file in each extension directory, to denote the mapping relationship between the local and remote localization files.

Welcome to contribute by PR or contact me to join the project. **Before translating, please read [TRANSLATING.md](TRANSLATING.md)** for the conventions, the glossary (source of truth), and reference works; see [TRANSLATION-GUIDANCE.md](TRANSLATION-GUIDANCE.md) for grammar rules with examples, the local MediaWiki glossary, and pitfalls. There is also a general-purpose glossary table we maintain here:
https://docs.google.com/spreadsheets/d/1zV0gl4TWV5fkf2r9i_1P1jmH_p7LOzbhZQgm7mPwDdE/edit?usp=sharing

### Japanese
これは、アイヌ語へのMediawiki翻訳プロジェクトです。現在、translatewikiはアイヌ語に対応していないため、登録に長い時間がかかることがわかっており、言語の承認もより難しいようです。現在は、ここでGitHubを使用して、生のJSONで書いて翻訳する他の方法を使用する必要があります。

`ain.json`ファイルは、いくつかのアイヌ語の翻訳が含まれている`ja.json`に基づいています。 `ja.json`および`en.json`ファイルは、Mediawikiパッケージの配布されたMediawikiパッケージの`mediawiki-1.41.0/languages/i18n`ディレクトリにあります。元の著者については、これらのファイルを参照してください。

また、各拡張機能ディレクトリにもローカライズファイルがあり、各拡張機能の配布パッケージにも`ain.json`、`ja.json`、`en.json`のような類似したファイル構造があります。後者の2つも、それぞれの拡張機能の配布パッケージにあります。元の著者については、これらのファイルを参照してください。また、各拡張機能ディレクトリには、ローカルとリモートのローカライズファイルのマッピング関係を示す`metadata.json`ファイルもあります。

参加するには、PRを出していただくか、参加ご連絡いただければ幸いです。**翻訳の前に、表記規則・用語集（典拠）・参考文献をまとめた [TRANSLATING.md](TRANSLATING.md) をお読みください。** 文法規則の作例・MediaWiki専用ローカル用語集・注意点については [TRANSLATION-GUIDANCE.md](TRANSLATION-GUIDANCE.md) をご覧ください。また、一般用の翻訳用語一覧表も以下のURLにて管理・公開しております。
https://docs.google.com/spreadsheets/d/1zV0gl4TWV5fkf2r9i_1P1jmH_p7LOzbhZQgm7mPwDdE/edit?usp=sharing

## Enable script conversion
To initialize script conversion, after uploading `AinConversion.php`, `LanguageConverter.php`, and `LanguageConverterData.php` automatically, go to shell and run `php maintenance/run.php generateLocalAutoload` to refresh `autoload` files.
