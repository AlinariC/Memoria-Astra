function Header(elem)
  if elem.level == 1 then
    local title = pandoc.utils.stringify(elem.content):lower()
    if title:match("^prologue") or title:match("^epilogue") or title:match("^dedication") or title:match("^acknowledgements") or title:match("^colophon") then
      elem.classes:insert('unnumbered')
    end
  end
  return elem
end
