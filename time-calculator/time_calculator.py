def add_time(start, duration, DOTW=None):

  start_time, meridian = start.split()
  start_hour, start_minute = map(int, start_time.split(':'))

  if meridian == 'PM' and start_hour != 12:
    start_hour += 12
  elif meridian == 'AM' and start_hour == 12:
    start_hour = 0

  duration_hour, duration_minute = map(int, duration.split(':'))

  end_minute = (start_minute + duration_minute) % 60
  end_hour = (start_hour + duration_hour +
              (start_minute + duration_minute) // 60) % 24
  end_meridian = 'AM' if end_hour < 12 else 'PM'

  if end_hour == 0:
    end_hour = 12
  elif end_hour > 12:
    end_hour -= 12

  days_later = (start_hour + duration_hour +
                (start_minute + duration_minute) // 60) // 24

  if DOTW:
    days = [
      'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
      'sunday'
    ]
    start_day_index = days.index(DOTW.lower())
    end_day_index = (start_day_index + days_later) % 7
    end_day = ', ' + days[end_day_index].capitalize()
  else:
    end_day = ''

  new_time = f"{end_hour:d}:{end_minute:02d} {end_meridian}{end_day}"
  if days_later == 1:
    new_time += ' (next day)'
  elif days_later > 1:
    new_time += f' ({days_later} days later)'
  return new_time
