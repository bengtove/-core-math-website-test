import contextlib
import io
import unittest

from scripts import build_open_opportunities as builder


class UrlExtractionTests(unittest.TestCase):
    def test_epsrc_bold_rich_values_resolve_to_same_url(self):
        expected = (
            "https://www.ukri.org/opportunity/"
            "mathematical-sciences-early-independence-fellowship/"
        )
        rich_values = {
            builder.COLUMNS["programme"]: (
                "**[Mathematical Sciences Early Independence Fellowship]"
                f"({expected})**"
            ),
            builder.INTERNAL_URL_COLUMN: f"**{expected}**",
        }

        url, source = builder.resolve_url(
            "Mathematical Sciences Early Independence Fellowship",
            rich_values,
        )

        self.assertEqual(url, expected)
        self.assertEqual(source, "matching_both")

    def test_only_complete_outer_bold_wrapper_is_unwrapped(self):
        self.assertEqual(
            builder.unwrap_outer_markdown_bold("**https://example.org/**"),
            "https://example.org/",
        )
        self.assertEqual(
            builder.unwrap_outer_markdown_bold("**https://example.org/"),
            "**https://example.org/",
        )

    def test_genuinely_different_urls_remain_a_conflict(self):
        rich_values = {
            builder.COLUMNS["programme"]: (
                "**[Example](https://example.org/first)**"
            ),
            builder.INTERNAL_URL_COLUMN: "**https://example.org/second**",
        }

        with contextlib.redirect_stdout(io.StringIO()):
            url, source = builder.resolve_url("Example", rich_values)

        self.assertIsNone(url)
        self.assertEqual(source, "conflict")


if __name__ == "__main__":
    unittest.main()
