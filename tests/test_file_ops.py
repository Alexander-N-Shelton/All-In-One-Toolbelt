# toolbelt/tests/test_date_utils.py

from logic.file_ops import get_all_items, delete_file, move_file


def test_get_all_items(tmp_path):
    """Test that all files and folders are returned from a directory."""
    # Setup
    (tmp_path / "folder").mkdir()
    (tmp_path / "file1.txt").write_text("hello")
    (tmp_path / "folder" / "file2.txt").write_text("world")

    expected = {
        str(tmp_path / "folder"),
        str(tmp_path / "file1.txt"),
        str(tmp_path / "folder" / "file2.txt")
    }

    actual = set(get_all_items(tmp_path))
    assert expected.issubset(actual)


def test_delete_file(tmp_path):
    """Test that a file is deleted successfully."""
    file = tmp_path / "file.txt"
    file.write_text("delete me")
    assert file.exists()
    delete_file(file)
    assert not file.exists()


def test_move_file(tmp_path):
    """Test that a file is moved successfully."""
    src = tmp_path / "src.txt"
    dst_dir = tmp_path / "dest"
    dst_dir.mkdir()
    src.write_text("move me")
    move_file(src, dst_dir)
    moved_file = dst_dir / "src.txt"
    assert moved_file.exists()
    assert moved_file.read_text() == "move me"
