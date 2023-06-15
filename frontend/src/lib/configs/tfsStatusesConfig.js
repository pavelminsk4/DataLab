const CARD_STATUSES = {
  PICKING: 'Picking',
  SUMMARY: 'Summary',
  QACHECK: 'Q&A Check',
  PUBLISHING: 'Publishing',
  PUBLISHED: 'Published',
  IRRELEVANT: 'Irrelevant',
}

export const defaultStatuses = [
  CARD_STATUSES.PICKING,
  CARD_STATUSES.SUMMARY,
  CARD_STATUSES.QACHECK,
  CARD_STATUSES.PUBLISHING,
  CARD_STATUSES.PUBLISHED,
  CARD_STATUSES.IRRELEVANT,
]

export const modalTabs = {
  [CARD_STATUSES.PICKING]: ['Original content'],
  [CARD_STATUSES.SUMMARY]: ['Original content', 'Summary'],
  [CARD_STATUSES.QACHECK]: ['Original content', 'Q&A Check'],
  [CARD_STATUSES.PUBLISHING]: ['Original content', 'Story report'],
}

export const dragAndDropStatuses = {
  [CARD_STATUSES.IRRELEVANT]: {
    status: CARD_STATUSES.IRRELEVANT,
    page: 1,
    color: '#797D80',
    isShow: false,
    allowedToDrag: [CARD_STATUSES.SUMMARY, CARD_STATUSES.IRRELEVANT],
  },
  [CARD_STATUSES.PICKING]: {
    status: CARD_STATUSES.PICKING,
    page: 1,
    color: '#2A7697',
    isShow: true,
    allowedToDrag: [CARD_STATUSES.SUMMARY, CARD_STATUSES.IRRELEVANT],
  },
  [CARD_STATUSES.SUMMARY]: {
    status: CARD_STATUSES.SUMMARY,
    page: 1,
    color: '#3746A6',
    isShow: true,
    allowedToDrag: [CARD_STATUSES.QACHECK, CARD_STATUSES.IRRELEVANT],
  },
  [CARD_STATUSES.QACHECK]: {
    status: CARD_STATUSES.QACHECK,
    page: 1,
    color: '#AB3E00',
    isShow: true,
    allowedToDrag: [
      CARD_STATUSES.SUMMARY,
      CARD_STATUSES.PUBLISHING,
      CARD_STATUSES.IRRELEVANT,
    ],
  },
  [CARD_STATUSES.PUBLISHING]: {
    status: CARD_STATUSES.PUBLISHING,
    page: 1,
    color: '#2A8500',
    isShow: true,
    allowedToDrag: [
      CARD_STATUSES.PUBLISHED,
      CARD_STATUSES.SUMMARY,
      CARD_STATUSES.QACHECK,
      CARD_STATUSES.IRRELEVANT,
    ],
  },
  [CARD_STATUSES.PUBLISHED]: {
    status: CARD_STATUSES.PUBLISHED,
    page: 1,
    color: '#961CCF',
    isShow: true,
    allowedToDrag: [],
  },
}

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
