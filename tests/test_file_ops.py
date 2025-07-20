from agent.tools import file_ops
import os

def test_list_files(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("sample")
    result = file_ops.list_files(str(tmp_path))
    assert result.success
    assert "test.txt" in result.data
