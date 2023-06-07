export const defaultStatuses = [
  'Picking',
  'Summary',
  'Q&A Check',
  'Publishing',
  'Published',
  'Irrelevant',
]

export const modalTabs = {
  Picking: ['Original content'],
  Summary: ['Original content', 'Summary'],
  'Q&A Check': ['Original content', 'Q&A Check'],
  Publishing: ['Original content', 'Story report'],
}

export const dragAndDropStatuses = [
  {
    status: 'Picking',
    page: 1,
    color: '#2A7697',
    allowedToDrag: ['Summary', 'Irrelevant'],
  },
  {
    status: 'Summary',
    page: 1,
    color: '#3746A6',
    allowedToDrag: ['Q&A Check', 'Irrelevant'],
  },
  {
    status: 'Q&A Check',
    page: 1,
    color: '#AB3E00',
    allowedToDrag: ['Summary', 'Publishing', 'Irrelevant'],
  },
  {
    status: 'Publishing',
    page: 1,
    color: '#2A8500',
    allowedToDrag: ['Published', 'Summary', 'Q&A Check', 'Irrelevant'],
  },
  {status: 'Published', page: 1, color: '#961CCF', allowedToDrag: []},
]

const SUMMARY = {
  color: '#3746A6',
  availableStatusesForMoving: [
    {title: 'Q&A Check', color: '#AB3E00'},
    {title: 'Irrelevant', color: '#797D80'},
  ],
}

const QACHECK = {
  color: '#AB3E00',
  availableStatusesForMoving: [
    {title: 'Publishing', color: '#168400'},
    {title: 'Summary', color: '#3746A6'},
    {title: 'Irrelevant', color: '#797D80'},
  ],
}

export const cardStatuses = {
  Picking: {
    color: '#2A7697',
    availableStatusesForMoving: [
      {title: 'Summary', color: '#3746A6'},
      {title: 'Irrelevant', color: '#797D80'},
    ],
  },
  Summary: SUMMARY,
  'Back to summary': SUMMARY,
  'Q&A Check': QACHECK,
  'Back to q&a Check': QACHECK,
  Publishing: {
    color: '#168500',
    availableStatusesForMoving: [
      {title: 'Published', color: '#961CCF'},
      {title: 'Summary', color: '#3746A6'},
      {title: 'Q&A Check', color: '#AB3E00'},
      {title: 'Irrelevant', color: '#797D80'},
    ],
  },
  Published: {
    color: '#961CCF',
    availableStatusesForMoving: [],
  },
  Irrelevant: {
    color: '#797D80',
    availableStatusesForMoving: [{title: 'Picking', color: '#2A7697'}],
  },
}
