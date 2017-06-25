"""SingleTable end to end testing on Linux/OSX."""

import pytest

from terminaltables import SingleTable
from terminaltables.terminal_io import IS_WINDOWS

pytestmark = pytest.mark.skipif(str(IS_WINDOWS))


def test_single_line():
    """Test single-lined cells."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
        ['Watermelon', 'green'],
        [],
    ]
    table = SingleTable(table_data, 'Example')
    table.inner_footing_row_border = True
    table.justify_columns[0] = 'left'
    table.justify_columns[1] = 'center'
    table.justify_columns[2] = 'right'
    actual = table.table

    expected = (
        '\033(0\x6c\033(BExample\033(0\x71\x71\x71\x71\x71\x77\x71\x71\x71\x71\x71\x71\x71\x77\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x6b\033(B\n'

        '\033(0\x78\033(B Name       \033(0\x78\033(B Color \033(0\x78\033(B      Type \033(0\x78\033(B\n'

        '\033(0\x74\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x75\033(B\n'

        '\033(0\x78\033(B Avocado    \033(0\x78\033(B green \033(0\x78\033(B       nut \033(0\x78\033(B\n'

        '\033(0\x78\033(B Tomato     \033(0\x78\033(B  red  \033(0\x78\033(B     fruit \033(0\x78\033(B\n'

        '\033(0\x78\033(B Lettuce    \033(0\x78\033(B green \033(0\x78\033(B vegetable \033(0\x78\033(B\n'

        '\033(0\x78\033(B Watermelon \033(0\x78\033(B green \033(0\x78\033(B           \033(0\x78\033(B\n'

        '\033(0\x74\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x75\033(B\n'

        '\033(0\x78\033(B            \033(0\x78\033(B       \033(0\x78\033(B           \033(0\x78\033(B\n'

        '\033(0\x6d\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x76\x71\x71\x71\x71\x71\x71\x71\x76\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x6a\033(B'
    )
    assert actual == expected


def test_multi_line():
    """Test multi-lined cells."""
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', 'Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\nDil Pickles'],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = SingleTable(table_data)

    # Test defaults.
    actual = table.table
    expected = (
        '\033(0\x6c\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x77\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6b\033(B\n'

        '\033(0\x78\033(B Show       \033(0\x78\033(B Characters                                                       '
        '                   \033(0\x78\033(B\n'

        '\033(0\x74\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x75\033(B\n'

        '\033(0\x78\033(B Rugrats    \033(0\x78\033(B Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille,'
        ' Angelica Pickles, \033(0\x78\033(B\n'

        '\033(0\x78\033(B            \033(0\x78\033(B Dil Pickles                                                      '
        '                   \033(0\x78\033(B\n'

        '\033(0\x78\033(B South Park \033(0\x78\033(B Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick       '
        '                   \033(0\x78\033(B\n'

        '\033(0\x6d\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x76\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6a\033(B'
    )
    assert actual == expected

    # Test inner row border.
    table.inner_row_border = True
    actual = table.table
    expected = (
        '\033(0\x6c\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x77\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6b\033(B\n'

        '\033(0\x78\033(B Show       \033(0\x78\033(B Characters                                                       '
        '                   \033(0\x78\033(B\n'

        '\033(0\x74\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x75\033(B\n'

        '\033(0\x78\033(B Rugrats    \033(0\x78\033(B Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille,'
        ' Angelica Pickles, \033(0\x78\033(B\n'

        '\033(0\x78\033(B            \033(0\x78\033(B Dil Pickles                                                      '
        '                   \033(0\x78\033(B\n'

        '\033(0\x74\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x75\033(B\n'

        '\033(0\x78\033(B South Park \033(0\x78\033(B Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick       '
        '                   \033(0\x78\033(B\n'

        '\033(0\x6d\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x76\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6a\033(B'
    )
    assert actual == expected

    # Justify right.
    table.justify_columns = {1: 'right'}
    actual = table.table
    expected = (
        '\033(0\x6c\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x77\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6b\033(B\n'

        '\033(0\x78\033(B Show       \033(0\x78\033(B                                                                  '
        '        Characters \033(0\x78\033(B\n'

        '\033(0\x74\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x75\033(B\n'

        '\033(0\x78\033(B Rugrats    \033(0\x78\033(B Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille,'
        ' Angelica Pickles, \033(0\x78\033(B\n'

        '\033(0\x78\033(B            \033(0\x78\033(B                                                                  '
        '       Dil Pickles \033(0\x78\033(B\n'

        '\033(0\x74\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x75\033(B\n'

        '\033(0\x78\033(B South Park \033(0\x78\033(B                          Stan Marsh, Kyle Broflovski, '
        'Eric Cartman, Kenny McCormick \033(0\x78\033(B\n'

        '\033(0\x6d\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x76\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6a\033(B'
    )
    assert actual == expected