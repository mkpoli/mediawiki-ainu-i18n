
<?php
/**
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 * http://www.gnu.org/copyleft/gpl.html
 *
 * @file
 */

/**
 * Ainu specific converter routine.
 *
 * Based on:
 *  - IuConverter.php
 * 	- EnConverter.php
 *  - ZhConverter.php
 *  - ainconv-py (https://github.com/mkpoli/ainconv-py/)
 * 
 * @ingroup Languages
 * 
 * @author mkpoli
 */
class AinConverter extends LanguageConverterSpecific {
    public $l2k = [
		"a" => "ア",
		"i" => "イ",
		"u" => "ウ",
		"e" => "エ",
		"o" => "オ",
		"á" => "ア",
		"í" => "イ",
		"ú" => "ウ",
		"é" => "エ",
		"ó" => "オ",
		"'a" => "ア",
		"'i" => "イ",
		"'u" => "ウ",
		"'e" => "エ",
		"'o" => "オ",
		"'á" => "ア",
		"'í" => "イ",
		"'ú" => "ウ",
		"'é" => "エ",
		"'ó" => "オ",
		"’a" => "ア",
		"’i" => "イ",
		"’u" => "ウ",
		"’e" => "エ",
		"’o" => "オ",
		"’á" => "ア",
		"’í" => "イ",
		"’ú" => "ウ",
		"’é" => "エ",
		"’ó" => "オ",
		"ka" => "カ",
		"ki" => "キ",
		"ku" => "ク",
		"ke" => "ケ",
		"ko" => "コ",
		"sa" => "サ",
		"si" => "シ",
		"su" => "ス",
		"se" => "セ",
		"so" => "ソ",
		"ta" => "タ",
		"tu" => "ト゚",
		"te" => "テ",
		"to" => "ト",
		"ca" => "チャ",
		"ci" => "チ",
		"cu" => "チュ",
		"ce" => "チェ",
		"co" => "チョ",
		"na" => "ナ",
		"ni" => "ニ",
		"nu" => "ヌ",
		"ne" => "ネ",
		"no" => "ノ",
		"ha" => "ハ",
		"hi" => "ヒ",
		"hu" => "フ",
		"he" => "ヘ",
		"ho" => "ホ",
		"pa" => "パ",
		"pi" => "ピ",
		"pu" => "プ",
		"pe" => "ペ",
		"po" => "ポ",
		"ma" => "マ",
		"mi" => "ミ",
		"mu" => "ム",
		"me" => "メ",
		"mo" => "モ",
		"ya" => "ヤ",
		"yi" => "イ",
		"yu" => "ユ",
		"ye" => "イェ",
		"yo" => "ヨ",
		"ra" => "ラ",
		"ri" => "リ",
		"ru" => "ル",
		"re" => "レ",
		"ro" => "ロ",
		"wa" => "ワ",
		"wi" => "ヰ",
		"we" => "ヱ",
		"wo" => "ヲ",
		"nn" => "ン",
		"tt" => "ッ",
	];

    public $l2k_coda = [
        "w" => "ゥ",
        "y" => "ィ",
        "m" => "ㇺ",
        "n" => "ㇴ",
        "s" => "ㇱ",
        "p" => "ㇷ゚",
        "t" => "ッ",
        "T" => "ㇳ",
        "k" => "ㇰ",
        "r" => [
            "a" => "ㇻ",
            "i" => "ㇼ",
            "u" => "ㇽ",
            "e" => "ㇾ",
            "o" => "ㇿ",
        ],
        "h" => [
            "a" => "ㇵ",
            "i" => "ㇶ",
            "u" => "ㇷ",
            "e" => "ㇸ",
            "o" => "ㇹ",
        ],
        "x" => [
            "a" => "ㇵ",
            "i" => "ㇶ",
            "u" => "ㇷ",
            "e" => "ㇸ",
            "o" => "ㇹ",
        ],
    ];


	public function getMainCode(): string {
		return 'ain';
	}

	public function getLanguageVariants(): array {
		return [ 'ain', 'ain-latn', 'ain-kana' ];
	}

	public function getVariantsFallbacks(): array {
		return [
			'ain' => 'ain-latn',
			'ain-latn' => 'ain',
			'ain-kana' => 'ain',
		];
	}
    
    public function getVariantNames() : array {
        $names = [
            'ain' => 'Aynu itak',
            'ain-latn' => 'Aynu itak (Rómaunkur Itak-itokpa)',
            'ain-kana' => 'アイヌ イタㇰ (カタカナ イタキトㇰパ)',
		];
        return array_merge( parent::getVariantNames(), $names );
    }

	protected function loadDefaultTables(): array {
		return [
			'ain' => new ReplacementArray(),
			'ain-latn' => new ReplacementArray(),
            'ain-kana' => new ReplacementArray(),
		];
	}

	function clean(string $text): string {
		// Assuming NFKC normalization is not needed or is handled elsewhere if necessary
		$text = str_replace(["-", "=", ".", ","], "", $text);
		return $text;
	}

    function separate_word(string $text): array {
        $vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'];
        $consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'];
        $syllableMap = [];
        $syllableCount = 1;
    
        for ($i = 0, $len = mb_strlen($text); $i < $len; $i++) {
            $char = mb_substr($text, $i, 1);
            if (in_array(mb_strtolower($char), $vowels)) {
                if ($i > 0 && in_array(mb_strtolower(mb_substr($text, $i - 1, 1)), $consonants)) {
                    $syllableMap[$i - 1] = $syllableCount;
                }
                $syllableMap[$i] = $syllableCount;
                $syllableCount++;
            }
        }
    
        for ($i = 0, $len = mb_strlen($text); $i < $len; $i++) {
            if (!isset($syllableMap[$i])) {
                $syllableMap[$i] = $syllableMap[$i - 1] ?? 0;
            }
        }
    
        $syllables = [];
        $currentGroupId = 1;
        $head = 0;
    
        for ($i = 0, $len = mb_strlen($text); $i < $len; $i++) {
            if (($syllableMap[$i] ?? 0) != $currentGroupId) {
                $currentGroupId = $syllableMap[$i];
                $syllables[] = mb_substr($text, $head, $i - $head);
                $head = $i;
            }
        }
    
        $syllables[] = mb_substr($text, $head);
    
        return array_map(function($s) { return str_replace("'", "", $s); }, $syllables);
    }

	function separate(string $text): array {
		if (empty($text)) {
			return [];
		}
	
		$result = [];
		$currentGroup = [];
		$lastAlpha = IntlChar::isalpha($text[0]);
	
		foreach (mb_str_split($text) as $char) {
			$currentAlpha = IntlChar::isalpha($char);
	
			if ($currentAlpha != $lastAlpha) {
				if (!empty($currentGroup)) {
					$joined = implode($currentGroup);
					if ($lastAlpha) {
						$result = array_merge($result, $this->separate_word($joined));
					} else {
						$result[] = $joined;
					}
					$currentGroup = [$char];
				} else {
					$currentGroup[] = $char;
				}
			} else {
				$currentGroup[] = $char;
			}
	
			$lastAlpha = $currentAlpha;
		}
	
		if (!empty($currentGroup)) {
			$joined = implode($currentGroup);
			if ($lastAlpha) {
				$result = array_merge($result, $this->separate_word($joined));
			} else {
				$result[] = $joined;
			}
		}
	
		return $result[0] !== '' ? $result : array_slice($result, 1);
	}

	function latn2kana(
		string $text,
		bool $use_wi = false,
		bool $use_we = false,
		bool $use_wo = false,
		bool $use_small_i = false,
		bool $use_small_u = false,
		bool $use_small_n = false
	): string {
		$syllables = $this->separate($text);

		$result = "";
	
		foreach ($syllables as $syllable) {
			$syllable = $this->clean(strtolower($syllable));

			if (!preg_match('/[a-zA-Záíúéó]/i', $syllable)) {

				$result .= $syllable;
				continue;
			}
	
            $before = $syllable;

			$syllable = str_replace(['á', 'é', 'í', 'ó', 'ú'], ['a', 'e', 'i', 'o', 'u'], $syllable);
	

			if (strlen($syllable) === 0) {
				continue;
			}
	
			$lastChar = $syllable[strlen($syllable) - 1];
	
			if (strpos('bcdfghjklmnpqrstvwxyz', $lastChar) !== false) {
				$remains = substr($syllable, 0, -1);
				$coda = $lastChar;
			} else {
				$remains = $syllable;
				$coda = '';
			}
	
			$convertedRemains = $this->l2k[$remains] ?? '';
	
			$result .= $convertedRemains;
	
            $nucleus = $remains ? $remains[strlen($remains) - 1] : null;

            $convertedCoda = '';

            if (array_key_exists($coda, $this->l2k_coda)) {
                if (is_array($this->l2k_coda[$coda])) {
                    $convertedCoda = $this->l2k_coda[$coda][$nucleus] ?? $this->l2k_coda[$coda]['u'];
                } else {
                    $convertedCoda = $this->l2k_coda[$coda];
                }
            } else {
                $convertedCoda = $coda;
            }

            $result .= $convertedCoda;
	
			if (!$use_small_i) {
				$result = str_replace("ィ", "イ", $result);
			}
			if (!$use_small_u) {
				$result = str_replace("ゥ", "ウ", $result);
			}
			if (!$use_small_n) {
				$result = str_replace("ㇴ", "ン", $result);
			}
	
			if (!$use_wi) {
				$result = str_replace("ヰ", "ウィ", $result);
			}
			if (!$use_we) {
				$result = str_replace("ヱ", "ウェ", $result);
			}
			if (!$use_wo) {
				$result = str_replace("ヲ", "ウォ", $result);
			}
		}

		return str_replace("’", "", $result);
	}

	function convertWord(string $text): string {
		preg_match_all('/[\p{Latin}=]+/u', $text, $matches);
		foreach ($matches[0] as $word) {
			if (ctype_upper(str_replace(['_'], '', $word))) {
				continue;
			}
			$text = str_replace($word, $this->latn2kana(strtolower($word)), $text);
		}
		return $text;
	}
	
	function convertSentence(string $text): string {
		// Preprocess
		$text = str_replace(['or ta', 'orta'], 'otta', $text);
	
		return implode(' ', array_map([$this, 'convertWord'], mb_split(' ', $text)));
	}

	
	public function makeUpper( $text ) {
		// Make the text uppercase for demonstration
		error_log( "makeUpper: $text" );
		return strtoupper( $text );
	}

	public function translate( $text, $toVariant ) {
		// Do not convert if the text is already in latin or not specified
		if ( $toVariant == 'ain-latn' || $toVariant == 'ain' ) {
			return $text;
		}

		// If $text is empty or only includes spaces, do nothing
		// Otherwise translate it
		if ( trim( $text ) ) {
			// $text = $this->makeUpper( $text );

			$text = $this->convertSentence( $text );
			// $this->loadTables();
			// // To syllabics, first translate uppercase to lowercase Latin
			// if ( $toVariant == 'ike-cans' ) {
			// 	$text = $this->mTables['lowercase']->replace( $text );
			// }
			// $text = $this->mTables[$toVariant]->replace( $text );
		}
		return $text;
	}

}
