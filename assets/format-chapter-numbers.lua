function Header(elem)
  if elem.level == 1 and elem.number and not elem.classes:includes('unnumbered') then
    local num = tostring(elem.number[1])
    if tonumber(num) < 10 then
      num = "0" .. num
    end
    local title = pandoc.utils.stringify(elem.content)
    elem.content = pandoc.List({
      pandoc.Str("Chapter " .. num .. ". " .. title)
    })
  end
  return elem
end
